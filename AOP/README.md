# AOP Logging Example (aop-logging)

Simple Spring Boot example demonstrating a logging aspect and a small greeting API.

**Key points**
- Demonstrates AOP logging via `LoggingAspect`.
- Provides a `GreetingService` and a small REST controller with endpoints.

**Prerequisites**
- Java 17+ (project tested with Java 23.0.1).
- Maven wrapper is included (`mvnw` / `mvnw.cmd`).

Getting started (Windows PowerShell)

1. Run tests:

```powershell
.\mvnw.cmd test
```

2. Run the application:

```powershell
.\mvnw.cmd spring-boot:run
```

3. Build an executable JAR:

```powershell
.\mvnw.cmd package
java -jar target\aop-logging-0.0.1-SNAPSHOT.jar
```

4. To see the greetings:

```Open in browser:
http://localhost:8080/greet?name=Trina
```

Important endpoints

- `GET /` — root greeting (returns a simple greeting). If you see a Whitelabel Error Page for `/`, the controller now provides a root mapping so this should return content.
- `GET /greet` — main greeting endpoint (optional query param `name`). Examples:
  - `http://localhost:8080/`
  - `http://localhost:8080/greet`
  - `http://localhost:8080/greet?name=Alice`

Configuration

- Application properties are in `src/main/resources/application.properties`.
- To change the server port, set `server.port` in `application.properties` or pass `-Dserver.port=<port>` when starting.

Logging

- Logs are configured to write to `logs/aop-logging.log` (see `application.properties`).
- The `LoggingAspect` logs method entry/exit for `GreetingService.greet(..)` in DEBUG/INFO levels.

Project structure (important packages)

- `com.example.aoplogging.logging` — AOP aspect(s) for logging.
- `com.example.aoplogging.service` — `GreetingService` implementation.
- `com.example.aoplogging.web` — `GreetingController` REST endpoints.

Quick run helper (`erun`)

You can use the included `erun` wrappers to start the application more conveniently from the project root:

- Windows CMD:

```powershell
.\erun.cmd
```

- PowerShell:

```powershell
.\erun.ps1
```

Both scripts call the bundled Maven wrapper (`mvnw.cmd`) to run `spring-boot:run`. You can pass additional arguments, for example to forward Maven properties:

```powershell
.\erun.cmd -Dspring-boot.run.jvmArguments="-Xmx512m"
.\erun.ps1 -Dspring-boot.run.jvmArguments="-Xmx512m"
```
- Both wrappers expect to be run from the project root where `mvnw.cmd` lives.
