from policyengine_us.model_api import *


class co_chp_lab_saving(Variable):
    value_type = float
    entity = Person
    label = "Colorado Child Health Plan Plus lab and imaging expense reduction"
    definition_period = YEAR

    def formula(person, period, parameters):
        income_level = person("medicaid_income_level", period)
        is_pregnant = person("is_pregnant", period)
        p = parameters(period).gov.states.co.hcpf.chp.copays.lab
        copay = where(is_pregnant, 0, p.calc(income_level))
        lab_expense = person("lab_expense", period)
        imaging_expense = person("imaging_expense", period)
        lab_saving = max_(0, lab_expense - copay)
        imaging_saving = max_(0, imaging_expense - copay)
        return lab_saving + imaging_saving
