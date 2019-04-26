from PageObjects.CommonPage import PageObject
from PageObjects.CuraPage import Cura
from PageObjects.OnboardingPage import Onboarding

page_object = PageObject()
cura = Cura()
onboarding = Onboarding()


@When("I start the onboarding flow")
def step(context):
    onboarding.startFlow()


@Step("the |any| page is shown with title '|any|'")
def step(context, _, expected_title):
    actual_title = onboarding.fetchPageTitle()
    test.compare(expected_title, actual_title)


@Step("I accept the user agreement")
def step(context):
    onboarding.acceptAgreement()


@Given("I'm on the |any| page of the onboarding flow")
def step(context, page):
    onboarding.verifyPage(page)


@When("I confirm the changelog changes")
def step(context):
    onboarding.navigateNextPage()


@When("I agree to my data being collected")
def step(context):
    onboarding.navigateNextPage()


@When("I finish the onboarding flow")
def step(context):
    onboarding.finishWizard()