from tkinter import *
import joblib
import numpy as np

# Load trained model and scaler
model = joblib.load("credit_card_approval_model.pkl")
scaler = joblib.load("scaler.pkl")

# Create main window
w = Tk()
w.title("Credit Card Approval Predictor")
w.geometry("400x650")
w.config(bg="lavender")

# Header
header = Label(text="Enter Applicant Details", font=("helvetica", 16, "bold"), bg="lavender", fg="navy")
header.pack(pady=10)

# Age
Label(w, text="Applicant Age:", bg="lavender").pack()
E_Age = Entry(w)
E_Age.pack()

# Years of Working
Label(w, text="Years of Working:", bg="lavender").pack()
E_years_of_working = Entry(w)
E_years_of_working.pack()

# Total Bad Debt
Label(w, text="Total Bad Debt:", bg="lavender").pack()
E_total_bad_debt = Entry(w)
E_total_bad_debt.pack()

# Total Good Debt
Label(w, text="Total Good Debt:", bg="lavender").pack()
E_total_good_debt = Entry(w)
E_total_good_debt.pack()

# Owned Realty
Label(w, text="Owned Realty:", bg="lavender").pack()
realty_var = StringVar(value="No")
Radiobutton(w, text="Yes", value="Yes", variable=realty_var, bg="lavender").pack()
Radiobutton(w, text="No", value="No", variable=realty_var, bg="lavender").pack()

# Owned Car
Label(w, text="Owned Car:", bg="lavender").pack()
car_var = StringVar(value="No")
Radiobutton(w, text="Yes", value="Yes", variable=car_var, bg="lavender").pack()
Radiobutton(w, text="No", value="No", variable=car_var, bg="lavender").pack()

# Income Type
Label(w, text="Income Type:", bg="lavender").pack()
income_var = StringVar(value="Working")
income_types = ["Pensioner", "State_servant", "Student", "Working"]
for income in income_types:
    Radiobutton(w, text=income, variable=income_var, value=income, bg="lavender").pack()

# Result Label
result_label = Label(w, text="", font=("helvetica", 14, "bold"), bg="lavender")
result_label.pack(pady=10)

# Predict Function
def predict():
    try:
        # Step 1: Collect inputs
        age = float(E_Age.get())
        years_working = float(E_years_of_working.get())
        bad_debt = float(E_total_bad_debt.get())
        good_debt = float(E_total_good_debt.get())

        # Step 2: Encode categorical values manually
        owned_realty = 1 if realty_var.get() == "Yes" else 0
        owned_car = 1 if car_var.get() == "Yes" else 0

        # One-hot encode Income Type manually (drop_first=True in training)
        income_input = income_var.get()
        income_options = ["Pensioner", "State_servant", "Student", "Working"]
        income_encoded = [1 if income_input == opt else 0 for opt in income_options]

        # Step 3: Combine all features
        input_data = [age, years_working, bad_debt, good_debt, owned_realty, owned_car] + income_encoded
        input_array = np.array(input_data).reshape(1, -1)

        # Step 4: Scale
        input_scaled = scaler.transform(input_array)

        # Step 5: Predict
        prediction = model.predict(input_scaled)

        # Step 6: Show result
        if prediction[0] == 1:
            result_label.config(text="Credit Card Approved ✅", fg="green")
        else:
            result_label.config(text="Credit Card Rejected ❌", fg="red")

    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="orange")

# Predict Button
Button(w, text="Predict", bg="blue", fg="white", command=predict).pack(pady=10)

w.mainloop()
