class mush():
  def __init__(self, conn, name):
    self.conn = conn
    self.name = name
  def fileno(self):
    return self.conn.fileno()
