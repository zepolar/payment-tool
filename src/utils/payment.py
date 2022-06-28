from exception.file_exception import EmptyError
from utils.constants import schedule
from utils.time import converter_time


def total_pay_calculation(lines):
    if not lines:
        raise EmptyError("File is empty. Nothing to do")
    else:
        result = {}
        for line in lines:
            split_line = line.strip().split("=")
            if len(split_line) > 1:
                unpack = {'Name': split_line[0],
                          'Payload': list(map(lambda payload: payload, split_line[-1].split(",")))}
                total_payment = []
                for item in unpack.get('Payload'):
                    total_payment.append(
                        daily_pay_calculation(item[:2], converter_time(item[2:7]),
                                              converter_time(item[8:])))
                result[unpack.get('Name')] = sum(total_payment)
        return result


def daily_pay_calculation(day, start, end):
    if start < end:
        if day in schedule.keys():
            return [v * (end.hour - start.hour) for (s, e, v) in schedule[day] if start >= s and end <= e].pop()
        else:
            raise ValueError("There exist an error with day")
    else:
        raise ValueError("The end time should be greater than start time")
