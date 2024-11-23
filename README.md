# Singleton Pattern Implementation in Python

This repository provides a simple implementation of the Singleton pattern in Python. The Singleton pattern ensures that only one instance of a class is created throughout the application and provides a global point of access to that instance.

## Features

	•	Thread-safe Singleton using a Lock.
	•	Simple and reusable design.
	•	Demonstrates how to ensure a single instance with shared state.

## Code Overview

The Singleton class:

	•	Uses the __new__ method to control instance creation.
	•	Ensures thread safety with a Lock.
	•	Shares the spark and log attributes between all instances.


## Use Cases

	•	Database Connections: Ensure only one connection pool is active.
	•	Logging: Maintain a single logging instance for consistent application-wide logs.
	•	Caching: Manage shared resources like in-memory cache.

## Contact
Feel free to reach out with any questions or feedback.

Linkedin: https://www.linkedin.com/in/vasilii-iagunov/
Email: iagunov.vasilii@gmail.com