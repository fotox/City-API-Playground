# V.I.K.I
## Log Module

### 1. Function
The function defines the type of logging in the entire V.I.K.I project.
The log output is defined as follows:

```
logging.Formatter(fmt='%(levelname)s | %(asctime)s | %(message)s', datefmt='%Y-%m-%dT%H:%M:%SZ')
```

```
ERROR | 2023-11-16T14:18:34Z | Test Message
```

In addition, the target module is defined when the module is initialized. This causes logged files to be saved in
the correct target folder.

When containerizing modules, the `log_module` must also be integrated. The paths to the log files are automatically
adapted to the new environment.

### 2. Directories
The `log_module` contains two directories. Current logs are saved in the `current` directory. The `archive` directory is
used to archive logs that were created at least on the previous day and filled with at least one log entry. These
archive files are saved in zip format with a day tag in the respective subdirectory of the archive folder up to a
maximum of 30 files.

### 3. Integration
To be able to use the module in other modules, import the logs_module as follows.

```python
from log_module.log_app import viki_log

logger = viki_log("<NAME OF MODULE>")
```
