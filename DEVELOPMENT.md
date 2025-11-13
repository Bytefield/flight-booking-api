# Flight Booking API - Development Notes

## Current Status (2025-11-13)

### ✅ What's Complete
- AWS SAM infrastructure setup
- 4 Lambda functions with proper structure
- 3 DynamoDB tables configured
- Local testing working with SAM CLI
- All code committed to git (commit: 0746c77)

### 🔧 How to Resume Development

#### Start Local Testing
```bash
# Activate virtualenv
source .venv/bin/activate

# Start SAM (use venv version to avoid Docker API issues)
.venv/bin/sam local start-api

# In another terminal, test endpoints
curl http://127.0.0.1:3000/flights
curl -X POST http://127.0.0.1:3000/auth/register
```

#### Important Note
Use `.venv/bin/sam` instead of system `sam` due to Docker API 1.44 patch.

### 📋 Next Steps (When You Resume)

1. **Implement Auth Handler** (src/auth/handler.py)
   - JWT token generation
   - Password hashing with bcrypt
   - User registration logic
   - Login validation

2. **Set Up Local DynamoDB** (Optional for testing)
   ```bash
   docker run -p 8000:8000 amazon/dynamodb-local
   ```

3. **Implement Bookings Handler** (src/bookings/handler.py)
   - Create booking logic
   - Check flight availability
   - Update seat counts
   - Cancel bookings

4. **Implement Users Handler** (src/users/handler.py)
   - JWT validation middleware
   - Get user profile
   - Update profile

5. **Deploy to AWS**
   ```bash
   sam build
   sam deploy --guided
   ```

### 🐛 Known Issues

- **Flights endpoint returns 500**: Needs local DynamoDB or AWS deployment
- **SAM CLI**: Must use `.venv/bin/sam` (patched for Docker API 1.44)

### 📚 Key Files

- `template.yaml` - SAM infrastructure definition
- `src/*/handler.py` - Lambda function code
- `samconfig.toml` - Deployment configuration (eu-north-1)
- `.gitignore` - Excludes .aws-sam/, .venv/, __pycache__/

### 🎓 What You Learned

- AWS Lambda event structure (body, headers, pathParameters)
- SAM CLI local testing workflow
- Docker container-based Lambda execution
- API Gateway integration patterns
- DynamoDB table design with GSI indexes
- Professional Python code standards (type hints, docstrings, PEP 8)

### 💡 Quick Commands

```bash
# Build project
sam build

# Start local API
.venv/bin/sam local start-api

# Test endpoints
curl http://127.0.0.1:3000/flights

# Deploy to AWS
sam deploy

# View logs
sam logs -n FlightsFunction --tail
```

---

**Status**: Paused at working local testing phase. Ready to implement handlers or deploy to AWS.
