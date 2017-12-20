# Tasks

Some general purpose automation scripts.

## Usage

`reminder.py` - Sends an email (using Gmail) when a deadline is within a week.

```
$ # Create a config.json file.
$ cat config.json
{
    "DEADLINE": "June 5, 2017"
    "DEADLINE_DESC": "Buy some gifts"
    "EMAIL": "myemail@gmail.com"
    "PASSWORD": "hunter2"
}
$ python reminder.py
# Sends an email when it's a week before the deadline.
```

## License

See the [license file](LICENSE)