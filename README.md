```
____    __    ____  __    __   _______ .______       _______   ______      
\   \  /  \  /   / |  |  |  | |   ____||   _  \     |   ____| /  __  \     
 \   \/    \/   /  |  |__|  | |  |__   |  |_)  |    |  |__   |  |  |  |    
  \            /   |   __   | |   __|  |      /     |   __|  |  |  |  |    
   \    /\    /    |  |  |  | |  |____ |  |\  \----.|  |____ |  `--'  '--. 
    \__/  \__/     |__|  |__| |_______|| _| `._____||_______| \_____\_____\
                                                                           
```

```

  ______   ______   .___  ___. .___  ___.      ___      .__   __.  _______   ______    _______     _______.
 /      | /  __  \  |   \/   | |   \/   |     /   \     |  \ |  | |       \ /  __  \  |   ____|   /       |
|  ,----'|  |  |  | |  \  /  | |  \  /  |    /  ^  \    |   \|  | |  .--.  |  |  |  | |  |__     |   (----`
|  |     |  |  |  | |  |\/|  | |  |\/|  |   /  /_\  \   |  . `  | |  |  |  |  |  |  | |   __|     \   \    
|  `----.|  `--'  | |  |  |  | |  |  |  |  /  _____  \  |  |\   | |  '--'  |  `--'  | |  |____.----)   |   
 \______| \______/  |__|  |__| |__|  |__| /__/     \__\ |__| \__| |_______/ \______/  |_______|_______/    
                                                                                                           
```


# whereq-commandoes

Welcome to **whereq-commandoes**, a collection of CLI tools built by **whereq**. This repository aims to provide a versatile toolset for developers, system admins, and automation enthusiasts. Each tool is designed to perform specific tasks with a focus on simplicity and efficiency.

## Index of CLI Tools

| Tool Name       | Description                                                            |
|-----------------|------------------------------------------------------------------------|
| [restman](#restman)     | A command-line tool for testing RESTful APIs and acting as a cURL alternative. |
| [clipman](#clipman) | A utility for managing clipboard content.   |
| [filecleaner](#filecleaner) | A utility for cleaning up unnecessary or temporary files from directories.   |
| [sysinfo](#sysinfo)     | A system information tool that displays hardware and software details.         |
| [dbmanager](#dbmanager)   | A lightweight CLI tool to manage database operations like backups, restores, and queries. |
| [netwatch](#netwatch)    | A network monitoring CLI tool for keeping track of local and remote connections. |

---

## CLI Tools Overview

### restman
`restman` is a command-line tool designed to test RESTful APIs, much like Postman but with a focus on command-line use. It supports various HTTP methods like GET, POST, PUT, and DELETE, and provides options for specifying HTTP headers, SSL certificates, and more.

**Features:**
- Supports HTTP methods (GET, POST, PUT, DELETE, etc.)
- SSL certificate handling
- Custom HTTP headers
- Verbose mode for detailed responses

**Usage Example:**
```bash
python restman.py get https://api.example.com/resource -H "Authorization: Bearer token"
```

You can find more details [here](restman/README.md).

---

### clipman

--- 

### filecleaner
`filecleaner` helps to clean up directories by removing unnecessary or temporary files, such as logs, cache files, or old backups.

**Features:**
- Customizable file patterns to delete (e.g., *.log, *.tmp)
- Recursive folder cleanup
- Dry-run mode to preview changes before deletion

You can find more details [here](filecleaner/README.md).

---

### sysinfo
`sysinfo` is a tool for gathering detailed information about the system’s hardware and software. It provides reports on CPU, memory, disk usage, and network configurations.

**Features:**
- CPU and memory usage reporting
- Disk space and partition details
- Network interface information

You can find more details [here](sysinfo/README.md).

---

### dbmanager
`dbmanager` is a lightweight database management CLI tool that handles database backups, restores, and basic queries.

**Features:**
- Backup and restore database functionality
- Execute SQL queries from the command line
- Support for MySQL, PostgreSQL, and SQLite

You can find more details [here](dbmanager/README.md).

---

### netwatch
`netwatch` monitors network connections, allowing you to track local or remote host activity, ping services, and display real-time network statistics.

**Features:**
- Monitor active connections
- Real-time network stats and bandwidth usage
- Ping and traceroute utilities

You can find more details [here](netwatch/README.md).

---

## How to Use

To use any tool in this repo, navigate to the corresponding folder and follow the instructions in its `README.md` for installation and usage.

Example:
```bash
cd restman
python restman.py --help
```

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you would like to improve any existing tool or add a new one.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

With **whereq-commandoes**, you can simplify your command-line workflows and automate complex tasks in an easy, maintainable way.

