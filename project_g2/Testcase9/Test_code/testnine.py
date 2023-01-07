from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import data
import pytest
import time

class Test_Hari:
    url = "https://opensource-demo.orangehrmlive.com"

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def test_login(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Hari_Selectors.input_box_username).send_keys(data.Hari_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Hari_Selectors.input_box_password).send_keys(data.Hari_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.pim_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.add_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Hari_Selectors.input_box_firstName).send_keys(data.Hari_Data.firstName)
        self.driver.find_element(by=By.NAME, value=data.Hari_Selectors.input_box_lastName).send_keys(data.Hari_Data.lastName)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.save_xpath).click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.job_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.joiningdate_xpath).send_keys('2019-05-16')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.jobtitle_xpath).click()
        time.sleep(4)
        executive_button=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.chiefexecutive_xpath).click()
        time.sleep(4)
        ActionChains(self.driver).click(on_element = executive_button).perform()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.jobcatgory_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.saleswork_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.subunit_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.salesmarkting_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.location_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.newyork_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.employeestatus_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.fulltime_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.radiobutton_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.contractstart_xpath).send_keys('2019-05-16')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.contractend_xpath).send_keys('2021-05-16')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.savebutton_xpath).click()
        time.sleep(5)
        assert self.driver.title == 'OrangeHRM'
