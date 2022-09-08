# diia_auth_server

Web server for comunicationg with ID gov ua


## Contents

  * [Synopsis](#synopsis)
  * [Dependencies](#dependencies)
    + [Critical Backends](#critical-backends)
    + [System Requirements](#system-requirements)
  * [Features](#features)
  * [API](#api)
  * [How To Guides](#how-to-guides)
    + [Setup](#setup)
      * [Setup on Host](#setup-on-host)
    + [Build](#build)
      * [Build on Host](#build-on-host)
      * [Build on Docker](#build-on-docker)
    + [Run](#run)
      * [Dev Server](#dev-server)
      * [Standalone](#standalone)
      * [Docker](#docker-container)
    + [Test](#test)
    + [Package](#package)
  * [Additional Resources](#additional-resources)


## Synopsis

```
bin/service {start|stop|status|restart}
```


## Dependencies

### Critical Backends

  * _[TODO: Add services, data stores and critical backends]_

### System Requirements

 * Please refer to the `requirements.txt` file and the `setup.py` script for a complete, up-to date, list of application requirements
 * The `requirements_dev.txt` file specified dependencies necessary for running the tests. See testing instructions below


## Features

  * _[TODO: Add list of user-facing features]_


## API

 * Swagger UI: [`http://0.0.0.0:9999/api/v1.0/docs`](http://0.0.0.0:9999/api/v1.0/docs)
 * OpenAPI Schema Definition: `diia_auth_server/docs/swagger-v1.0.yaml` 


## How To Guides

### Setup

#### Setup on Host

Configure the app:

```bash
cp config/default.conf ~/.config/diia_auth_server.conf
```

Install the app:

```bash
$ make clean install
```

Make sure you have the database user/passwords in your `~/.pgpass` file.

### Build

#### Build on Host

```bash
$ make clean install
```

#### Build on Docker

```bash
$ make docker-build
```

### Run

#### Dev Server

Development server is strictly for development purposes only. It comes with neat support for file-watching and automatic hot-reload.

```bash
$ make dev-server
```

#### Standalone

To run the application as a standalone service in the background (SysV style), run the following command. All logs are redirected to the `logs/diia_auth_server.log` file.

```bash
$ bin/service start
```

#### Docker Container

```bash
$ make docker-run
```

The above command assumes the docker image has been built, to make sure you have built it already, please run the following command:

```bash
$ make docker-build
```

### Test

```
$ make test
```

### Package

```
$ make package
```

The result of the command is a wheel binary under the `dist/` local directory.

## Additional Resources

  * _[TODO: Add any relevant additional resources to the project]_
