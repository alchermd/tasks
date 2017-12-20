# Tasks

Some general purpose automation scripts.

## Usage

`reminder.py` - Sends an email (using Gmail) when a deadline is within a week.

```
$ export DEADLINE='June 5, 2017'
$ export DEADLINE_DESC='Buy some gifts'
$ export EMAIL='myemail@gmail.com'
$ python reminder.py
# Sends an email when it's a week before the deadline.
```

## License

See the [license file](LICENSE)