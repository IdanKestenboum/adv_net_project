# SEED Labs - Slow HTTP/TCP DDoS Attack and Mitigation Lab

## Student Implementation Version

This is the student implementation version of the SEED Labs DDoS attack and mitigation lab. Students are required to complete two simple coding tasks to demonstrate their understanding of the key concepts.

## Lab Overview

This lab demonstrates slow HTTP/TCP DDoS attacks and their mitigation using HAProxy. Students will learn about slow POST attacks, understand how they can exhaust server resources, and implement protection mechanisms using path-based bypass rules and IP-based throttling with stick tables.

## Prerequisites

- Basic understanding of HTTP protocol and TCP connections
- Familiarity with Docker and containerization
- Knowledge of networking concepts (IP addresses, ports, connections)
- Basic Linux command-line experience
- Basic Python programming knowledge

## Lab Environment

The lab uses Docker containers to create an isolated environment with:

- **nginx-server**: Backend web server (port 8080)
- **haproxy**: Reverse proxy with DDoS protection (port 8081)
- **attacker**: Container with attack scripts
- **user**: Container for legitimate user simulation

## Implementation Tasks

### Task 1: HAProxy Configuration Implementation

Students must complete the following tasks in `haproxy/haproxy.cfg`:

1. **Task 1.1**: Define a stick table for tracking abusive IPs
2. **Task 1.2**: Define ACL for abusive IPs

### Task 2: Attack Script Implementation

Students must complete the following tasks in `attacker/slow_post_threads.py`:

1. **Task 2.1**: Implement target host and port selection
2. **Task 2.2**: Implement slow data transmission

## Setup Instructions

1. **Clone and Navigate**:
   ```bash
   cd seed-proxy-lab
   ls -la
   ```

2. **Build and Start Containers**:
   ```bash
   docker-compose up -d --build
   docker-compose ps
   ```

3. **Verify Services**:
   ```bash
   curl http://localhost:8080  # nginx
   curl http://localhost:8081  # haproxy
   ```

## Testing Your Implementation

### Step 1: Verify HAProxy Configuration
```bash
# Check HAProxy configuration syntax
docker exec -it haproxy haproxy -c -f /usr/local/etc/haproxy/haproxy.cfg

# If successful, restart HAProxy
docker-compose restart haproxy
```

### Step 2: Test Attack Script
```bash
# Access attacker container
docker exec -it attacker bash

# Test the attack script
python3 slow_post_threads.py proxy protected
```

### Step 3: Verify Protection
```bash
# Access user container
docker exec -it user sh

# Test legitimate access during attack
curl -s http://haproxy:8081/
```

## Evaluation Criteria

### Implementation Tasks (60%)
- **HAProxy Configuration (30%)**: Correct implementation of stick table and ACL
- **Attack Script (30%)**: Correct implementation of target selection and slow data transmission

### Testing and Validation (40%)
- **Configuration Validation (20%)**: HAProxy configuration compiles and runs without errors
- **Attack Effectiveness (20%)**: Attack script successfully demonstrates DDoS and protection mechanisms

## Submission Requirements

### Required Deliverables
1. Completed `haproxy.cfg` file with all TODO tasks implemented
2. Completed `slow_post_threads.py` file with all TODO tasks implemented
3. Screenshots showing successful compilation and testing
4. Brief report explaining your implementation choices

### Submission Format
Submit the following files:
1. `haproxy.cfg` - Your completed HAProxy configuration
2. `slow_post_threads.py` - Your completed attack script
3. `implementation_report.pdf` - Brief report (1-2 pages) explaining your implementation
4. Screenshots of successful testing (as separate image files)

## File Structure

```
seed-proxy-lab/
├── README.md                           # This file
├── seed-manual.tex                     # Student implementation manual
├── docker-compose.yml                  # Docker Compose configuration
├── nginx-server.Dockerfile            # Nginx server Dockerfile
├── haproxy/
│   ├── Dockerfile                     # HAProxy Dockerfile
│   └── haproxy.cfg                    # HAProxy configuration (with TODO tasks)
├── attacker/
│   ├── Dockerfile                     # Attacker container Dockerfile
│   └── slow_post_threads.py           # Attack script (with TODO tasks)
└── user/
    └── Dockerfile                     # User container Dockerfile
```

## Troubleshooting

### Common Issues
1. **Container won't start**: Check Docker daemon and available resources
2. **Connection refused**: Verify ports are not in use by other services
3. **Attack not working**: Ensure containers are on the same network
4. **HAProxy errors**: Check configuration syntax and file permissions

### Debug Commands
```bash
# Check container status
docker-compose ps

# View container logs
docker logs haproxy
docker logs nginx-server

# Test connectivity
docker exec -it user ping nginx-server
docker exec -it attacker ping haproxy

# Check HAProxy configuration
docker exec -it haproxy haproxy -c -f /usr/local/etc/haproxy/haproxy.cfg
```

## References

1. HAProxy Documentation: https://www.haproxy.org/download/2.6/doc/intro.txt
2. SEED Labs: https://seedsecuritylabs.org
3. Slowloris Attack: https://en.wikipedia.org/wiki/Slowloris_(computer_security)
4. DDoS Protection Strategies: https://www.cloudflare.com/learning/ddos/
