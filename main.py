def calculate_discount(order_amount):
    if order_amount >= 500_000:
        return 0.2  # 20 درصد تخفیف
    elif order_amount >= 300_000:
        return 0.1  # 10 درصد تخفیف
    elif order_amount >= 100_000:
        return 0.05  # 5 درصد تخفیف
    else:
        return 0

def notify_customer(name, order_amount):
    discount = calculate_discount(order_amount)
    discount_amount = order_amount * discount
    final_amount = order_amount - discount_amount

    message = f"""سلام {name} عزیز 🌟
سفارش شما به مبلغ {order_amount:,} تومان ثبت شد.
شما {discount * 100:.0f}% تخفیف گرفتید یعنی {discount_amount:,} تومان!
مبلغ قابل پرداخت: {final_amount:,} تومان 😊"""
    
    print(message)

