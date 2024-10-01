"""
Email Validator Utility

This module provides an EmailValidator class for validating and normalizing email addresses.

Usage:
  validator = EmailValidator()
  if validator.validate(email):
    normalized_email = validator.normalize(email)
"""

import re

class EmailValidator:
  
  """
  Suggestion #1: robustness & corrrectness
  in validate() function, email validation process
  is done according to some developer-defined conditions
  such as ('@' should be in email), or (local part length
  must be between 1-64)
  Instead of creating such conditions, benefiting from
  imported but not used regex package.
  And instead of coming up with some validation ideas, it's
  better to research about it and apply the state-of-art
  email validation algorithms
  """
  def validate(self, email):
    """Validates an email address."""
    
    """
    Suggestion #2: consistency
    All validation conditions (the dev came up with) is returning
    True or False.
    However, first if-statement checks if parameter email is a string.
    If it's not a string, then it raises an Exception unlike the rest
    of the code. This might mislead of confuse the client code.
    Instead of raising an Error, it can return False since a non-string
    email parameter is also not a valid email.
    """
    if not isinstance(email, str):
      raise ValueError("Email must be a string")
    if "@" not in email:
      return False
    localpart, domain = email.split("@")
    if len(localpart) < 1 or len(localpart) > 64:
      return False  
    return True


  """
  Suggestion #3: Single Responsibility Principle
  normalize() function returns the normalized version of the parameter email
  as expected.
  However, it does perform more than one operation on the email parameter. It
  is also very obvious from the inline comments:
    # remove leading...
    # remove dots...
    # convert domain...
  Instead of performing three operations in a single function, those can be
  migrated to another function. This migration would cause codes to be easier
  to test and apply the S of SOLID principles. 
  """
  def normalize(self, email):
    """Normalizes an email address."""
    # remove leading/trailing whitespace
    email = email.strip()
    
    # remove dots from localpart
    localpart, domain = email.split("@")
    localpart.replace(".", "")

    # convert domain to lowercase
    normalized = f"{localpart}@{domain.lower()}"
    return normalized

if __name__ == "__main__":
  validator = EmailValidator()
  
  """
  Suggestion #4: Object-oriented approach / OCP
  It is better to handle below email string literals 
  as Email objects. This approach would provide us
  convenience and simplicity especially in future, as
  the project grows. One possible object-oriented approach
  would be making an Email dataclass as it would store the
  email value. Upon that point, child classes or related
  classes will be easier. We will have more control over the
  classes and apply the Open-Closed Principle easier, thanks
  to the encapsulation.
  """

  emails = [
    "alice@example.com",
    "bob.smith@example.com",
    "invalid.email",
    "toolonglocalpartxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@example.com",
    "   carol@example.com   "
  ]

  for email in emails:
    if validator.validate(email):
      print(f"Valid: {email}")
      normalized = validator.normalize(email)
      print(f"Normalized: {normalized}")
    else:
      print(f"Invalid: {email}")
