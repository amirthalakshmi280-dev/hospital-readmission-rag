# Secure Coding Knowledge

## 1. Protect Sensitive Information

Do not store passwords, API keys, tokens, or private patient information directly in source code.

## 2. Input Validation

Always validate user input before processing it.

Example: Check whether the entered age is valid before using it.

## 3. Password Security

Passwords should never be stored as plain text.

Use secure password hashing techniques when storing passwords.

## 4. Avoid Hardcoded Secrets

Do not write passwords, API keys, or other secrets directly in source code.

Use environment variables or a secure secret manager instead.

## 5. Database Security

Use parameterized queries instead of directly joining user input into SQL queries.

## 6. File Security

Validate file names and file paths before accessing files.

## 7. Error Messages

Do not expose sensitive system information in error messages.

## 8. Dependency Security

Keep software dependencies updated and use trusted packages.

## 9. Medical Data Security

Medical information is sensitive.

Do not upload real patient records, names, medical IDs, or other private information to a public repository.

Use synthetic or anonymized data for educational projects.

## 10. Security Testing

Review code regularly for:

- Exposed secrets
- Invalid input
- Unsafe file access
- Insecure database queries
- Dependency vulnerabilities

## Summary

Secure coding reduces vulnerabilities and protects users, applications, and sensitive information.
