

##  :suspect: Usage

```bash
usage: hhunt [-h] [-t USER_TARGETS [USER_TARGETS ...]]
              [-u USER_URLS [USER_URLS ...]] [-q USER_QUERY] [--loose]
              [-c CONFIG_FILE [CONFIG_FILE ...]] [-o OUTPUT_FILE]
              [-j OUTPUT_JSON] [-bc BC_PATH] [-sk]
              [-k CLI_APIKEYS [CLI_APIKEYS ...]]
              [-lb LOCAL_BREACH_SRC [LOCAL_BREACH_SRC ...]]
              [-gz LOCAL_GZIP_SRC [LOCAL_GZIP_SRC ...]] [-sf]
              [-ch [CHASE_LIMIT]] [--power-chase] [--hide] [--debug]
              [--gen-config]

Email information and password lookup tool

optional arguments:
  -h, --help            show this help message and exit
  -t USER_TARGETS [USER_TARGETS ...], --targets USER_TARGETS [USER_TARGETS ...]
                        Either string inputs or files. Supports email pattern
                        matching from input or file, filepath globing and
                        multiple arguments
  -u USER_URLS [USER_URLS ...], --url USER_URLS [USER_URLS ...]
                        Either string inputs or files. Supports URL pattern
                        matching from input or file, filepath globing and
                        multiple arguments. Parse URLs page for emails.
                        Requires http:// or https:// in URL.
  -q USER_QUERY, --custom-query USER_QUERY
                        Perform a custom query. Supports username, password,
                        ip, hash, domain. Performs an implicit "loose" search
                        when searching locally
  --loose               Allow loose search by disabling email pattern
                        recognition. Use spaces as pattern seperators
  -c CONFIG_FILE [CONFIG_FILE ...], --config CONFIG_FILE [CONFIG_FILE ...]
                        Configuration file for API keys. Accepts keys from
                        Snusbase, WeLeakInfo, Leak-Lookup, HaveIBeenPwned,
                        Emailrep, Dehashed and hunterio
  -o OUTPUT_FILE, --output OUTPUT_FILE
                        File to write CSV output
  -j OUTPUT_JSON, --json OUTPUT_JSON
                        File to write JSON output
  -bc BC_PATH, --breachcomp BC_PATH
                        Path to the breachcompilation torrent folder. Uses the
                        query.sh script included in the torrent
  -sk, --skip-defaults  Skips Scylla and HunterIO check. Ideal for local scans
  -k CLI_APIKEYS [CLI_APIKEYS ...], --apikey CLI_APIKEYS [CLI_APIKEYS ...]
                        Pass config options. Supported format: "K=V,K=V"
  -lb LOCAL_BREACH_SRC [LOCAL_BREACH_SRC ...], --local-breach LOCAL_BREACH_SRC [LOCAL_BREACH_SRC ...]
                        Local cleartext breaches to scan for targets. Uses
                        multiprocesses, one separate process per file, on
                        separate worker pool by arguments. Supports file or
                        folder as input, and filepath globing
  -gz LOCAL_GZIP_SRC [LOCAL_GZIP_SRC ...], --gzip LOCAL_GZIP_SRC [LOCAL_GZIP_SRC ...]
                        Local tar.gz (gzip) compressed breaches to scans for
                        targets. Uses multiprocesses, one separate process per
                        file. Supports file or folder as input, and filepath
                        globing. Looks for 'gz' in filename
  -sf, --single-file    If breach contains big cleartext or tar.gz files, set
                        this flag to view the progress bar. Disables
                        concurrent file searching for stability
  -ch [CHASE_LIMIT], --chase [CHASE_LIMIT]
                        Add related emails from hunter.io to ongoing target
                        list. Define number of emails per target to chase.
                        Requires hunter.io private API key if used without
                        power-chase
  --power-chase         Add related emails from ALL API services to ongoing
                        target list. Use with --chase
  --hide                Only shows the first 4 characters of found passwords
                        to output. Ideal for demonstrations
  --debug               Print request debug information
  --gen-config, -g      Generates a configuration file template in the current
                        working directory & exits. Will overwrite existing
                        hhunt_config.ini file

```

-----

## :hurtrealbad: Usage examples

###### Query for a single target

```bash
$ hhunt -t target@example.com
```

###### Query for list of targets, indicate config file for API keys, output to `pwned_targets.csv`
```bash
$ hhunt -t targets.txt -c config.ini -o pwned_targets.csv
```

###### Query a list of targets against local copy of the Breach Compilation, pass API key for [Snusbase](https://snusbase.com/) from the command line
```bash
$ hhunt -t targets.txt -bc ../Downloads/BreachCompilation/ -k "snusbase_token=$snusbase_token"
```

###### Query without making API calls against local copy of the Breach Compilation
```bash
$ hhunt -t targets.txt -bc ../Downloads/BreachCompilation/ -sk
```

###### Search every .gz file for targets found in targets.txt locally, skip default checks

```bash
$ hhunt -t targets.txt -gz /tmp/Collection1/ -sk
```

###### Check a cleartext dump for target. Add the next 10 related emails to targets to check. Read keys from CLI

```bash
$ hhunt -t admin@evilcorp.com -lb /tmp/4k_Combo.txt -ch 10 -k "hunterio=ABCDE123"
```
###### Query username. Read keys from CLI

```bash
$ hhunt -t JSmith89 -q username -k "dehashed_email=user@email.com" "dehashed_key=ABCDE123"
```

###### Query IP. Chase all related targets. Read keys from CLI


```bash
$ hhunt -t 42.202.0.42 -q ip -c hhunt_config_priv.ini -ch 2 --power-chase
```

###### Fetch URL content (CLI + file). Target all found emails


```bash
$ hhunt -u "https://pastebin.com/raw/EPe2pakW" "list_of_urls.txt"
```


-----

