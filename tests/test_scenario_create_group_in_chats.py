# # test scenario ID 5: 1) create a chat group that consists of the user already logged in and
# # two other participants selected by their names
# # (group title and icon are not specified in this scenario and generated automatically)
# # 2) check that the group chat was opened after creation, consists of 3 people, and autogenerated title is correct
# # 3) check that the group can be found later in the list of all chats using a search field
#
#
# import allure
# from allure_commons.types import AttachmentType
# from tests.test_data import TestData
# from pages.dasboard_page import DashboardPage
# from pages.chat_page import ChatPage
# from config import Urls
# import time
# import pytest
#
#
# class TestScenarioCreateGroupInChats:
#
#     # @allure.feature('Group Chat')
#     # @allure.story('Create a group chat with 2 other participants selected; title and icon generated automatically')
#     # @allure.severity('critical')
#     @pytest.mark.parametrize("two_usernames", TestData.two_usernames_for_group_chat)
#     @pytest.mark.smoke
#     @pytest.mark.regression
#     def test_create_group_in_chats_with_two_users(self, browser, admin_login, two_usernames):
#         dashboard_page = DashboardPage(browser, Urls.dashboard_page)
#         dashboard_page.navigate_to_chats()
#
#         chats_page = ChatPage(browser, Urls.chats_page)
#         # chats_page.expand_chats()
#
#         chats_page.open_chat_group_creation()
#         # chats_page.collapse_chats()
#
#         chats_page.open_dropdown_with_participants_to_chose()
#         chats_page.select_participant_for_chat_group(two_usernames[0])
#         time.sleep(2)
#         chats_page.select_participant_for_chat_group(two_usernames[1])
#
#         chats_page.save_participants_selected_for_group_chat()
#         chats_page.save_group()
#
#         expected_group_title = two_usernames[0] + '+' + two_usernames[1]
#         actual_group_title = chats_page.get_name_of_chat_opened()
#         assert actual_group_title == expected_group_title, f"Wrong result (expected group title: \'{expected_group_title}\', actual: {actual_group_title}"
#
#         participants_number_shown = chats_page.get_number_of_group_chat_participants()
#         assert participants_number_shown == 3, f"Wrong result (expected: 3, actual: {participants_number_shown})"
#
#         # TODO: maybe check that all elements of chat window is present?
#         #  and send a message to verify that it works?
#         #  and also find the group created using chat search field?
