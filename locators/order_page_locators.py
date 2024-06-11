from selenium.webdriver.common.by import By
class OrderPageLocators:

    ORDER_FEED_HEADING = (By.XPATH, "//h1[text() = 'Лента заказов']")
    FIRST_ORDER = (By.XPATH, "//ul[@class = 'OrderFeed_list__OLh59']/li[1]/a[@class = 'OrderHistory_link__1iNby']")
    CLOSE_ORDER_INFO_BUTTON = (By.XPATH, "//div[@class = 'Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']/following-sibling::button[@type = 'button']")
    ORDER_LIST = (By.XPATH, "//ul[@class = 'OrderFeed_list__OLh59']")
    COUNTER_ORDERS_FOR_ALLTIME = (By.XPATH, "//p[text() = 'Выполнено за все время:']/following-sibling::p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']")
    COUNTER_ORDERS_FOR_ALLDAY = (By.XPATH, "//p[text() = 'Выполнено за сегодня:']/following-sibling::p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDER_IN_WORK = (By.XPATH, "//ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']")
    NO_ORDERS_IN_WORK  = (By.XPATH, "//li[text() = 'Все текущие заказы готовы!']")