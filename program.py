import os
import signal
import subprocess


def is_running(pgm):
    """Check if a program (pgm) is running"""
    if pgm.lower() == 'netflix':
        pgm = 'chrome'
    proc = subprocess.Popen(['pgrep', pgm], stdout=subprocess.PIPE)
    pids = [pid for pid in proc.stdout]
    if not len(pids):
        proc = subprocess.Popen(['pgrep', pgm.capitalize()], stdout=subprocess.PIPE)
        pids = [pid for pid in proc.stdout]
    return len(pids) > 0


def start_pgm(pgm):
    """Start a program (pgm)"""
    subprocess.Popen(pgm, stdout=subprocess.PIPE)


def stop_pgm(pgm):
    """Stop a program (pgm)"""
    for pgm in (pgm, pgm.capitalize()):
        proc = subprocess.Popen(['pgrep', pgm], stdout=subprocess.PIPE)
        for pid in proc.stdout:
            pid = int(pid.decode().strip('\n'))
            os.kill(pid, signal.SIGTERM)
