import numpy as np
from sklearn.linear_model import LinearRegression

class MathModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, data, target):
        self.model.fit(data, target)

    def predict(self, coefficients):
        return self.model.predict(coefficients)

# Example usage:
if __name__ == '__main__':
    data = np.array([[2, 3, 4], [5, 7, 10]])
    target = np.array([1, 1])
    
    model = MathModel()
    model.train(data, target)
    
    # Simulate prediction for an equation like "2x^2 + 3x + 4"
    prediction = model.predict(np.array([[2, 3, 4]]))
    print(f"Prediction: {prediction}")
