# PortMapper

**A Custom TCP Port Scanner for Network Reconnaissance**

PortMapper is a lightweight Python-based TCP port scanner designed for network reconnaissance and security testing. It efficiently scans target hosts to identify open ports and potential entry points.

## Features

- 🚀 Fast TCP port scanning
- 🎯 Configurable port range scanning
- ⏱️ Built-in timeout handling for closed ports
- 🛡️ Robust error handling (keyboard interrupts, DNS errors, connection errors)
- 📊 Clean and informative output
- 💻 Cross-platform compatibility

## Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses built-in libraries only)

## Installation
```bash
git clone https://github.com/krinathakkar646/PortMapper.git
cd portmapper
```

## Usage

### Basic Usage

Edit the `target` variable in the script to specify your target host:
```python
target = "scanme.nmap.org"  # Change this to your target
```

Then run:
```bash
python portmapper.py
```

### Customizing Port Range

Modify the range in the script:
```python
for port in range(1, 100):  # Scan ports 1-99
```

Change to:
```python
for port in range(1, 1001):  # Scan ports 1-1000
```

### Example Output
```
--------------------------------------------------
SCANNING TARGET : scanme.nmap.org
TIME STARTED : 2024-12-06 14:30:45.123456
--------------------------------------------------
Port 22 is Open 
Port 80 is Open 
Port 443 is Open 
--------------------------------------------------
[*] Scan Complete.
```

## How It Works

1. **Target Definition**: Specifies the hostname or IP address to scan
2. **Socket Creation**: Creates TCP sockets for connection attempts
3. **Port Scanning**: Iterates through specified port range
4. **Connection Testing**: Attempts to connect to each port with a 1-second timeout
5. **Result Reporting**: Displays open ports in real-time

## Code Structure
```python
import sys
import socket
from datetime import datetime

# Define target
target = "scanme.nmap.org"

# Display banner with scan information
# Create socket connection for each port
# Test connectivity and report open ports
# Handle errors gracefully
```

## Error Handling

The scanner includes comprehensive error handling for:
- **Keyboard Interrupt (Ctrl+C)**: Gracefully exits the program
- **DNS Resolution Errors**: Handles invalid hostnames
- **Connection Errors**: Manages network connectivity issues

## Legal Disclaimer

⚠️ **IMPORTANT**: This tool is intended for **authorized security testing and educational purposes only**. 

- Always obtain **explicit written permission** before scanning any network or system
- Unauthorized port scanning may be **illegal** in your jurisdiction
- The author is **not responsible** for misuse of this tool
- Use responsibly and ethically

**Only scan systems you own or have permission to test** (e.g., scanme.nmap.org is provided by Nmap for testing purposes).

## Common Use Cases

- Network security auditing
- Vulnerability assessment
- Network troubleshooting
- Educational purposes and learning
- Security research

## Limitations

- Currently scans TCP ports only (no UDP support)
- Sequential scanning (not multithreaded)
- Basic port detection (no service identification)
- Manual target configuration required

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## Roadmap

Potential future enhancements:
- [ ] Command-line argument support
- [ ] Multiple target scanning
- [ ] Service version detection
- [ ] JSON/CSV output formats
- [ ] Multithreading for faster scans
- [ ] UDP port scanning support
- [ ] Port range specification via CLI
- [ ] Save results to file

## Version History

- **v1.0** (December 2024) - Initial release with basic TCP port scanning

## Troubleshooting

### "Hostname could not be resolved"
- Check your internet connection
- Verify the target hostname is correct
- Try using an IP address instead

### "Could not connect to server"
- Check your network connection
- Verify firewall settings
- Ensure target is accessible from your network

### Slow scanning
- Reduce timeout value (currently 1 second)
- Reduce port range
- Check network latency

## Author

**Krina Thakkar**
- GitHub: [@krinathakkar646](https://github.com/krinathakkar646)

## Acknowledgments

- Thanks to the Python community for excellent documentation
- Inspired by Nmap and other network scanning tools
- Special thanks to scanme.nmap.org for providing a legal testing target

## Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the troubleshooting section above

## Disclaimer

This tool is provided "as is" without warranty of any kind. Use at your own risk. The author assumes no liability for any misuse or damage caused by this program.

---

**⭐ If you find this project useful, please consider giving it a star on GitHub!**
