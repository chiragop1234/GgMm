import subprocess
import os

# Kill existing tmate sessions
subprocess.run(["pkill", "-9", "tmate"])

# Download tmate release
subprocess.run(["wget", "-nc", "https://github.com/tmate-io/tmate/releases/download/2.4.0/tmate-2.4.0-static-linux-i386.tar.xz"], stdout=subprocess.DEVNULL)

# Extract tmate archive
subprocess.run(["tar", "--skip-old-files", "-xvf", "tmate-2.4.0-static-linux-i386.tar.xz"], stdout=subprocess.DEVNULL)

# Create a new tmate session
subprocess.run(["rm", "-f", "nohup.out"])
subprocess.run(["bash", "-ic", 'nohup ./tmate-2.4.0-static-linux-i386/tmate -S /tmp/tmate.sock new-session -d & disown -a'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Wait for tmate to be ready
subprocess.run(["./tmate-2.4.0-static-linux-i386/tmate", "-S", "/tmp/tmate.sock", "wait", "tmate-ready"])

# Display tmate SSH connection information
result = subprocess.run(["./tmate-2.4.0-static-linux-i386/tmate", "-S", "/tmp/tmate.sock", "display", "-p", '#{tmate_ssh}'], stdout=subprocess.PIPE)
tmate_ssh_info = result.stdout.decode().strip()

print("TMATE SSH Information:", tmate_ssh_info)
