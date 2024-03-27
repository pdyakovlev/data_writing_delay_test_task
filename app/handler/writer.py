import time


class Writer:
    def write(self,
              format: int,
              filename: str,
              id: int,
              recieve_time: time = None,) -> None:
        """Cервис-записи запросов в 2 txt файла."""
        with open(f'{filename}.txt', 'a') as f:
            if recieve_time is None:
                recieve_time = time.strftime('%H:%M:%S')
            if format == 1:
                write_time = time.strftime('%H:%M:%S')
                f.write(f'| {id} | {recieve_time} | {write_time} |\n')
            else:
                f.write(f'| {id} | {recieve_time} |\n')
