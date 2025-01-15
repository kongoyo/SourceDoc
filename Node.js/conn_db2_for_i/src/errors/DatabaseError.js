class DatabaseError extends Error {
  constructor(message, operation, originalError) {
    super(message);
    this.name = 'DatabaseError';
    this.operation = operation;
    this.originalError = originalError;
  }
}

module.exports = DatabaseError; 