param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Args
)

Write-Host "Running application via Maven wrapper..."

if (Test-Path -Path .\mvnw.cmd) {
    & .\mvnw.cmd spring-boot:run @Args
} else {
    Write-Error "mvnw.cmd not found. Run this from the project root where mvnw.cmd exists."
    exit 1
}
