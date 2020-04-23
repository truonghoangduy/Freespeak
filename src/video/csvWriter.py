import csv
import os
import logging

class CsvWriter:
  def __init__(self, filename, labels):
    super().__init__()
    self.filename = os.path.join('outputFiles', filename)
    self.labels = labels
    self.open = False

  def __enter__(self):
    self.start()
    return self

  def __exit__(self, type, value, traceback):
    self.stop()

  def start(self):
    logging.info('starting csv writer ' + self.filename)
    self.file = open(self.filename, mode='w', newline='')
    self.writer = csv.writer(
            self.file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    self.writer.writerow(self.labels)
    self.file.flush()
    self.open = True

  def stop(self):
    self.open = False
    self.file.close()
    logging.info('csv writer ' + self.filename + 'closed')

  def writerows(self, rows):
    if self.open:
      for row in rows:
        self.writer.writerow(row)
      self.file.flush()
