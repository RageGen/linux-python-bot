import subprocess
import psutil
from os import getenv
def run_command(command):
    sudo_password = getenv('SUDO_PASSWORD')
    command = f"echo {sudo_password} | sudo -S {command}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

def service_manager(service_name, action):
    match action:
        case 'info':
            command = f'systemctl is-active {service_name}'
            stdout, stderr = run_command(command)
            return f"Service {service_name} is {'active' if stdout.strip() == 'active' else 'not running'}" if not stderr else f"Error getting status of service {service_name}: {stderr}"
        case 'stop':
            command = f'sudo systemctl stop {service_name}'
            stdout, stderr = run_command(command)
            return f"Service {service_name} stopped." if not stderr else f"Error stopping service {service_name}: {stderr}"
        case 'restart':
            command = f'sudo systemctl restart {service_name}'
            stdout, stderr = run_command(command)
            return f"Service {service_name} restarted." if not stderr else f"Error restarting service {service_name}: {stderr}"
        case 'start':
            command = f'sudo systemctl start {service_name}'
            stdout, stderr = run_command(command)
            return f"Service {service_name} started." if not stderr else f"Error starting service {service_name}: {stderr}"
        case _:
            return 'Unknown action'

def process_manager(process_name, action):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            break
    match action:
        case 'info':
            return f"pid: {process.pid} name: {process.name()} cpu_usage: {process.cpu_percent(interval=1.0)} memory_usage: {process.memory_info()}"
        case 'kill':
            process.kill()
            return f"Process {process_name} killed."
        case 'start':
            process = subprocess.Popen(process_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return f"Process {process_name} started with PID: {process.pid}"
        case _:
            return 'Unknown action'

def reboot_system():
    command = 'reboot'
    stdout, stderr = run_command(command)
    return f"System is rebooting..." if not stderr else f"Error rebooting system: {stderr}"
def shutdown_system():
    command = 'shutdown -r now'
    stdout,stderr = run_command(command)
    return f"System is shutting" if not stderr else f"Error shutting down: {stderr}"
def get_system_info():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    network_io = psutil.net_io_counters()
    return f"CPU usage: {cpu_usage}%\nMemory usage: {memory_usage}%\nDisk usage: {disk_usage}%\nNetwork I/O: {network_io}"

def determine_entity_type(name):
    command = f'systemctl status {name}'
    stdout, stderr = run_command(command)
    return "service" if 'Loaded: not-found' not in stdout and 'could not be found' not in stderr else "process"

