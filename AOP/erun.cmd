@echo off
REM Simple wrapper to run the Spring Boot app using the bundled Maven wrapper (Windows CMD)
REM Usage: .\erun.cmd [additional mvn args]

if exist mvnw.cmd (
  call .\mvnw.cmd spring-boot:run %*
) else (
  echo mvnw.cmd not found. Make sure you're running this from the project root.
  exit /b 1
)
