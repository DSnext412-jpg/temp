 
import matplotlib.pyplot as plt
payment_methods=["UPI","Credit Card","Debit Card","Cash","Net Banking"] 
customers=[150,80,60,40,30] 
plt.figure(figsize=(8,6))
plt.pie(customers,labels=payment_methods,autopct="%1.1f%%",startangle=90)
plt.title("Preferred Payment Methods Among Customers") 
plt.show()