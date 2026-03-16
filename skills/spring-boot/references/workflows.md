# Spring Boot workflows

## Establish the target

- confirm Spring Boot and Java version
- confirm API, MVC, messaging, or hybrid app style
- confirm data-access posture
- confirm deployment and operational model

## Day-two workflow

- start from configuration and bean wiring clarity
- keep controllers and listeners thin
- make transactions, retries, and integration boundaries explicit
- verify build, tests, and deployment packaging after changes

## Common commands

```bash
./mvnw test
./mvnw spring-boot:run
./mvnw package
```

```bash
./gradlew test
./gradlew bootRun
```

## Verification

- run the project test suite and one local startup path such as `./mvnw test spring-boot:run` or `./gradlew test bootRun`
- confirm configuration binding, validation, transactions, and actuator visibility still match the operational contract
- verify controller, service, and repository boundaries by exercising one real request or message flow end-to-end

## Troubleshooting and recovery

- if bean wiring becomes confusing, simplify configuration first and let one module own the integration boundary before adding more annotations
- if transactions or retries drift, move them back to the service boundary and re-test the smallest failing use case
- if environments diverge, compare profiles, property sources, and container assumptions before changing application logic
