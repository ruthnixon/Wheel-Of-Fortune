//This is the class definition of a shopping cart object.

class ShoppingCart(var items: MutableMap<Item, Int>, var total: Float){

    // The code below is a function of the shopping cart class that adds a new item to the items map.

    fun addItem(newItem: Item, quantity: Int) {
        if (newItem !in items){
            items.put(newItem, quantity)
        }
        else{
            items.set(newItem, (items.getValue(newItem) + quantity))
        }
        total += newItem._getPrice() * quantity.toFloat()
    }

    // This code is a function of the shopping cart class that removes an item from the items map.

    fun removeItem(toRemove: Item, quantity: Int){

        var _quantity = quantity
        if (_quantity >= items.getValue(toRemove)){
            _quantity = items.getValue(toRemove)
            items.remove(toRemove)
        }
        else{
            items.set(toRemove, (items.getValue(toRemove) - quantity))
        }

        total -= (toRemove._getPrice() * _quantity)
    }

    // This is a toString function that prints out the content of the object in a string.

    override fun toString(): String {
        return "{Items: " + items.toString() + ", Total: " + total + "} "
    }
}

// /This is the class definition for the item object.

class Item(var price: Float, val name: String, val weight: Float, val type: String){

    // This is a function of the item class that changes the value of the price variable.
    fun changePrice(newPrice: Float){
        price = newPrice
    }

    // This is also a function of the item class that returns the value the items price. If the item is fruit or
    //vegetable, it calculates the price by multipling the price times the weight.

    fun _getPrice():Float{
        if (type.equals("fruit") or type.equals("vegetable")){
            return (price * weight)
        }
        else {
            return price
        }
    }

    // This is a toString function that prints out the content of the object in a string.
    override fun toString(): String {
        return "{Price: " + price + ", Name: " + name + ", Weight: " + weight + ", Type: " + type + "} "
    }
}

// This function loops and provides the options for the user. Based on the input the user provides, it calls
// certain functions.
fun shop(merchandise: MutableList<Item>, cart: ShoppingCart){
    var running = true
    var input = ""
    while(running){
        println("Welcome to the shopping program! Select from the following")
        println("1. View merchandise")
        println("2. Add to cart")
        println("3. Remove from cart")
        println("4. View cart")
        println("5. Purchase Items in cart")
        input = readLine()!!
        println()

        if (input.equals("1")){
            println(merchandise.toString())
        }
        else if (input.equals("2")){
            println("What is the index of the item you would like to add to your cart? ")
            var index = readLine()
            println("How many of this item do you want to add? ")
            var quantity = readLine()
            cart.addItem(merchandise.get(index!!.toInt() - 1), quantity!!.toInt())
            println("Added to cart.")
        }
        else if (input.equals("3")){
            println("What is the index of the item you would like to remove from your cart? ")
            var index = readLine()
            println("How many of this item do you want to remove? ")
            var quantity = readLine()
            if (merchandise.get(index!!.toInt()) in cart.items) {
                cart.removeItem(merchandise.get(index!!.toInt() - 1), quantity!!.toInt())
                println("Removed from cart.")
            }
        }
        else if (input.equals("4")){
            println(cart.toString())
        }
        else if (input.equals("5")){
            checkout(cart)
            return
        }
        println()
    }
}

// This function takes in a cart object, prints the total due, and asks the user for the payment. It also calculates
// change or if a user still needs to pay more.

fun checkout(cart: ShoppingCart) {
    var payment = ""
    var change = 0.0.toFloat()
    println("Your total is: $" + cart.total)
    while(true){
        println("Please type your payment amount: ")
        payment = readLine()!!
        change = payment.toFloat() - cart.total
        if (change > 0){
            println("You are due $" + change)
            return
        }
        else if (change == 0.0.toFloat()){
            println("Thank you. Have a nice day.")
            return
        }
        else
        {
            println("Your remaining balance is " + (change * (-1).toFloat()))
        }
    }
}

fun main()
{
    // Creating item objects to be used in the shopping function.

    val banana = Item(.50.toFloat(), "banana".toString(), 4.0.toFloat(), "fruit".toString())
    val milk = Item(2.15.toFloat(), "milk".toString(), 137.6.toFloat(), "beverage".toString())
    val chips = Item(3.50.toFloat(), "chips".toString(), 16.0.toFloat(), "snack".toString())
    val cereal = Item(4.0.toFloat(), "cereal".toString(), 17.637.toFloat(), "breakfast food".toString())

    // In here we are creating a list that will store the items for sale in a list.

    var merchandise = mutableListOf<Item>()

    merchandise.add(banana)
    merchandise.add(milk)
    merchandise.add(chips)
    merchandise.add(cereal)

    // This creates a map that will be used in my cart object.

    var map = mutableMapOf<Item, Int>()
    val myCart = ShoppingCart(map, 0.0.toFloat())
    //myCart.addItem(milk, 2)
    //myCart.addItem(banana, 3)
    //myCart.addItem(chips, 2)
    println(myCart.toString())
    shop(merchandise, myCart)
}

main()