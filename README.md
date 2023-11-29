# Google Style Pre-Commit Hook

A [pre-commit](http://pre-commit.com/) hook which will run Google's java code style formatter for you on your code!

Usage:

```
repos:
- repo: https://github.com/Poeschl/google-style-precommit-hook
  rev: <insert tag version here>
    hooks:
      - id: google-style-java
```

The script stores the Google formater Jar file in a folder called `.cache`.
You will probably want to add that folder to your ignore files.

## Additional config

The version of the used Google formatter can be set with arguments.
The Default is shown [here](https://github.com/Poeschl/google-style-precommit-hook/blob/master/google_style_format/__init__.py#L8)

```
- id: google-style-java
  args: [--version, 1.17.0]
```
