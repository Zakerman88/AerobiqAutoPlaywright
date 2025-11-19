from playwright.sync_api import Page, Locator

class DragAndDrop:

    def __init__(self, page: Page):
        self.page = page

    def dragndrop_program(self, drag: Locator, drop: Locator, dnd_xpath_locator: str, dnd_attribute_: str, dnd_text_: str):
        # Get the bounding box of the drag element to move mouse to its center
        drag_box = drag.bounding_box()
        self.page.mouse.move(drag_box['x'] + drag_box['width'] / 2, drag_box['y'] + drag_box['height'] / 2)
        self.page.mouse.down()

        # Wait until the text is NOT present in the element's attribute
        self.page.wait_for_function(
            f"""() => {{
                const elem = document.evaluate('{dnd_xpath_locator}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                if (!elem) return true;
                const attrValue = elem.getAttribute('{dnd_attribute_}') || '';
                return !attrValue.includes('{dnd_text_}');
            }}""",
            timeout=10000
        )

        # Get the bounding box of the drop element
        drop_box = drop.bounding_box()
        self.page.mouse.move(drop_box['x'] + drop_box['width'] / 2, drop_box['y'] + drop_box['height'] / 2)
        self.page.mouse.up()

    def dragndrop_judges(self, drag: Locator, drop: Locator, dnd_xpath_locator: str, dnd_attribute_: str, dnd_text_: str):
        # Get the bounding box of the drag element to move mouse to its center
        drag_box = drag.bounding_box()
        self.page.mouse.move(drag_box['x'] + drag_box['width'] / 2, drag_box['y'] + drag_box['height'] / 2)
        self.page.mouse.down()

        # The wait is commented out in the original, so omitting it here
        # If needed, uncomment and adjust similar to dragndrop_program
        # self.page.wait_for_function(
        #     f"""() => {{
        #         const elem = document.evaluate('{dnd_xpath_locator}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        #         if (!elem) return false;
        #         const attrValue = elem.getAttribute('{dnd_attribute_}') || '';
        #         return attrValue.includes('{dnd_text_}');
        #     }}""",
        #     timeout=10000
        # )

        # Get the bounding box of the drop element
        drop_box = drop.bounding_box()
        self.page.mouse.move(drop_box['x'] + drop_box['width'] / 2, drop_box['y'] + drop_box['height'] / 2)
        self.page.mouse.up()