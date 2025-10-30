from main import Menu, Order


def test_edit_price():
    m = Menu()
    m.menu = {"Pizza": 12}

    m.edit_price("Pizza", 20)

    assert m.menu["Pizza"] == 20.0


def test_edit_price_not_found():
    m = Menu()
    m.menu = {"Pizza": 12}

    m.edit_price("Cat", 20)

    assert "Cat" not in m.menu
    assert len(m.menu) == 1


def test_edit_price_negative():
    m = Menu()
    m.menu = {"Pizza": 12}

    m.edit_price("pizza", -10)

    assert m.menu["Pizza"] == 12


def test_add_menu():
    m = Menu()
    m.menu = {}

    m.add_menu("Pizza", 12.5)

    assert "Pizza" in m.menu
    assert m.menu["Pizza"] == 12.5


def test_add_menu_empty():
    m = Menu()
    m.menu = {}

    m.add_menu(" ", 12.5)

    assert len(m.menu) == 0


def test_add_menu_negative_price():
    m = Menu()
    m.menu = {}

    m.add_menu("pizza", -10)

    assert "Pizza" not in m.menu


def test_add_menu_duplicate():
    m = Menu()
    m.menu = {"Pizza": 12.5}
    m.add_menu("pizza", 10)

    assert len(m.menu) == 1


def test_add_menu_invalid_price(capsys):
    m = Menu()
    m.menu = {}
    m.add_menu("Burger", "abc")

    assert "Burger" not in m.menu

    out = capsys.readouterr().out
    assert "Invalid Price! Please Enter A Valid Number." in out


def test_view_menu(capsys):
    m = Menu()
    m.menu = {"Burger": 12, "Pizza": 16}
    m.view_menu()

    out = capsys.readouterr().out
    assert "1. Burger - 12" in out
    assert "2. Pizza - 16" in out


def test_view_menu_empty(capsys):
    m = Menu()
    m.menu = {}
    m.view_menu()

    out = capsys.readouterr().out
    assert "Menu Is Empty." in out


def test_remove_menu():
    m = Menu()
    m.menu = {"Burger": 12, "Pizza": 16}
    m.remove_menu("burger")

    assert len(m.menu) == 1
    assert "Burger" not in m.menu


def test_remove_menu_not_found(capsys):
    m = Menu()
    m.menu = {"Burger": 12, "Pizza": 16}
    m.remove_menu("cat")

    out = capsys.readouterr().out
    assert "Cat Was Not Found In The Menu!" in out

    assert len(m.menu) == 2
    assert "Burger" in m.menu
    assert "Pizza" in m.menu


def test_add_order():
    menu = {"Pizza": 12.5, "Burger": 10}
    o = Order(menu)
    o.add_order("Pizza", "2")
    assert "Pizza" in o.order
    assert o.order["Pizza"] == 2


def test_add_order_existing_item():
    menu = {"Pizza": 12.5, "Burger": 10}
    o = Order(menu)
    o.order = {"Pizza": 1}
    o.add_order("Pizza", "3")
    assert o.order["Pizza"] == 4


def test_add_order_item_not_in_menu(capsys):
    menu = {"Pizza": 12.5}
    o = Order(menu)
    o.add_order("Burger", "1")
    out = capsys.readouterr().out
    assert "Burger Is Not In The Menu!" in out
    assert "Burger" not in o.order


def test_add_order_invalid_quantity(capsys):
    menu = {"Pizza": 12.5}
    o = Order(menu)
    o.add_order("Pizza", "abc")
    out = capsys.readouterr().out
    assert "Quantity Should Be A Number!" in out
    assert "Pizza" not in o.order


def test_view_order_empty(capsys):
    menu = {"Pizza": 12.5}
    o = Order(menu)
    o.view_order()
    out = capsys.readouterr().out
    assert "Order Is Empty." in out


def test_view_order_with_items(capsys):
    menu = {"Pizza": 12.5, "Burger": 10}
    o = Order(menu)
    o.order = {"Pizza": 2, "Burger": 1}
    o.view_order()
    out = capsys.readouterr().out
    assert "1) Pizza, Qty:2, Price:25.0" in out
    assert "2) Burger, Qty:1, Price:10" in out
    assert "Total: 35.0" in out


def test_remove_order():
    menu = {"Pizza": 12.5, "Burger": 10}
    o = Order(menu)
    o.order = {"Pizza": 2, "Burger": 1}
    o.remove_order("Pizza")
    assert "Pizza" not in o.order
    assert "Burger" in o.order


def test_remove_order_not_in_order(capsys):
    menu = {"Pizza": 12.5, "Burger": 10}
    o = Order(menu)
    o.order = {"Pizza": 2}
    o.remove_order("Burger")
    out = capsys.readouterr().out
    assert "Burger Is Not In The Order." in out
    assert "Pizza" in o.order
