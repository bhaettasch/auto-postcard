class Connector:
    def __init__(self, params):
        """
        Constructor

        :param params: dict information to customize postcard

        Params:
        receiver_name
        sender_name

        receiver_gender (male, female, neutral)
        sender_gender

        lang (DE, EN, ...)

        formal (true, false)

        vacation_location
        vacation_startdate (timestamp)
        vacation_enddate (timestamp)
        """
        self.params = params
        self.init()

    def get_text(self):
        """
        Generate portion of text
        :return: generated text
        """
        return ""

    def init(self):
        """
        Init this generator (after self.params is set)
        """
        pass


class LookupMixin:
    """
    Lookup best-suited string based on params
    Classes using this mixin need to define an array self.lookup_table that contains (condition, string)-tuples
    """

    def find_best_mix(self):
        """
        Find best match
        :return: String with best condition match or empty string if no string with matching conditions exists
        """
        # Loop over all tuples
        for conditions, s in self.lookup_table:
            # Return the first string where all conditions match
            if all(self.params[param_name] == param_value for param_name, param_value in conditions.items()):
                return s
        return ""

    def get_text(self):
        return self.find_best_mix()
