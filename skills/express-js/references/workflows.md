# Express.js workflows

## Establish the target

- confirm Express and Node versions
- confirm API-only or mixed web-app scope
- confirm auth and session posture
- confirm deployment and reverse-proxy model

## Day-two workflow

- start from router ownership and middleware order
- validate input before business logic runs
- separate HTTP concerns from domain workflows
- verify startup, health checks, and proxy assumptions after changes

## Common commands

```bash
npm run dev
npm test
npm start
```

```bash
NODE_ENV=production node server.js
curl -i http://localhost:3000/health
```

## Verification

- run the test suite and a local server start, then exercise one real route with representative validation, auth, and error paths
- confirm middleware order, request parsing, error handling, and response shaping still behave in the intended sequence
- verify logging, health endpoints, and deployment assumptions after changes to server wiring or startup

## Troubleshooting and recovery

- if request handling starts to feel tangled, move validation, auth, and business orchestration back into separate middleware or services
- if routes behave differently after refactors, inspect router mounting order and error middleware placement before rewriting handlers
- if tests are noisy, stabilize them around HTTP behavior and serialized responses rather than internal middleware implementation details
