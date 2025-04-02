# GitHub Actions CI/CD Pipeline Documentation

This documentation provides an overview of integrating Pytest, Coverage, SonarQube, Render, and Slack into your GitHub Actions pipeline.

##  Prerequisites
- A GitHub repository
- Docker Hub account (for containerized applications)
- SonarCloud account (for code quality analysis)
- Render account (for deployment)
- Slack workspace (for notifications)

---

##  Running Pytest in GitHub Actions
Pytest is a testing framework for Python applications.

### **Steps**:
1. Install `pytest` in your project:
   ```sh
   pip install pytest
   ```
2. Create a `tests/` directory and add test cases.
3. Add the following to your GitHub Actions workflow:
   ```yaml
   - name: Run tests with pytest
     run: pytest --junitxml=reports/test-results.xml
   ```

**More info**: [Pytest Docs](https://docs.pytest.org/en/latest/)

---

##  Coverage Integration
Coverage helps track the percentage of code tested.

### **Steps**:
1. Install coverage:
   ```sh
   pip install coverage
   ```
2. Modify the test command in the GitHub Actions workflow:
   ```yaml
   - name: Run tests with coverage
     run: |
       coverage run -m pytest
       coverage xml -o coverage.xml
   ```
3. Upload the coverage report:
   ```yaml
   - name: Upload coverage report
     uses: actions/upload-artifact@v4
     with:
       name: coverage-report
       path: coverage.xml
   ```

 **More info**: [Coverage Docs](https://coverage.readthedocs.io/en/latest/)

---

## SonarQube Integration
SonarQube analyzes code quality and security vulnerabilities.

### **Steps**:
1. Get a SonarCloud token from [SonarCloud](https://sonarcloud.io/).
2. Store it as `SONAR_TOKEN` in GitHub secrets.
3. Add the following job to your workflow:
   ```yaml
   - name: SonarQube Scan
     run: |
       sonar-scanner \
         -Dsonar.organization=my-org \
         -Dsonar.projectKey=my-project \
         -Dsonar.host.url=https://sonarcloud.io \
         -Dsonar.login=${{ secrets.SONAR_TOKEN }}
   ```
 **More info**: [SonarQube Docs](https://docs.sonarqube.org/)

---

## Deploying to Render
Render is a cloud hosting platform for deploying web applications.

### **Steps**:
1. Get your **Deploy Hook ID** from [Render Dashboard](https://dashboard.render.com/).
2. Store it in GitHub Secrets as `RENDER_DEPLOY_HOOK`.
3. Add the deployment step to your workflow:
   ```yaml
   - name: Deploy to Render
     run: |
       curl -X POST \
         -H "Authorization: Bearer ${{ secrets.RENDER_API_KEY }}" \
         -H "Content-Type: application/json" \
         -d '{"dockerImage":"${{ secrets.DOCKER_USERNAME }}/todo-app:$GITHUB_SHA"}' \
         https://api.render.com/deploy/${{ secrets.RENDER_DEPLOY_HOOK }}
   ```

**More info**: [Render Docs](https://render.com/docs/)

---

##  Slack Notifications
Slack can notify your team when a build succeeds or fails.

### **Steps**:
1. Create a **Slack Incoming Webhook** from [Slack API](https://api.slack.com/messaging/webhooks).
2. Store it in GitHub secrets as `SLACK_WEBHOOK_URL`.
3. Add the notification step:
   ```yaml
   - name: Notify Slack
     uses: rtCamp/action-slack-notify@v2
     env:
       SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK_URL }}
       SLACK_MESSAGE: "Deployment Completed Successfully!"
   ```

**More info**: [Slack Webhooks](https://api.slack.com/messaging/webhooks)

---

## Summary
This guide covers:
- **Pytest** for testing
- **Coverage** for test reporting
- **SonarQube** for code analysis
- **Render** for deployment
- **Slack** for notifications

**Enhancements**:
- Add **Docker** to containerize the app
- Use **GitHub Secrets** for secure configurations
- Automate deployment workflows 

Need help? Check the official documentation:
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [SonarQube Docs](https://docs.sonarqube.org/)
- [Render Docs](https://render.com/docs/)
- [Slack Webhooks](https://api.slack.com/messaging/webhooks)

---

