# Commands

Below are list of commands along with its description.

```
make build
```

This command will install required dependencies for making a build of this
software. If your intention is to run tests or make a developer build then you
should perform `make build-dev`.


```
make build-dev
```

This command will install developer requirements. You should perform this step
if your goal is to make a developer build of this software.


```
make build-static
```

This command will update if existing Javascript dependencies are outdated or
install if it is not installed. After installation it will collect them at
`static` folder.


```
make unit-test
```

This command will run Python based unit test tests. Make sure you have already
performed the step to make a developer build.


```
make test
```

This command will run all tests which includes unit level of test and then
functional tests.


```
make run
```

This command will update Javascript dependencies and start the development
server at 5000 port.

```
make migrate
```

This command will apply exiting migrations to a new db. Make sure you have
performed the `make build-dev` step which is installing expected Python
dependencies.

```
make create-migrations
```

This command will create new migrations. You should perform this step when you
are modifying existing models. This command will update existing migrations
files to match whatever schema has for models. You should commit changes done at
`migrations` folder at your version control system.
