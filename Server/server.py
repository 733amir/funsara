import cherrypy
from database import Database

# Lowest version of android application that user should have.
APP_VERSION = 1


class Server:
    def __init__(self):
        self.db = Database()
        self.db.connect()

    def get_last_batch_number(self):
        """Run a query on funsara database to get most recent batch number from server."""
        return self.db.run(('SELECT MAX(number) FROM batches',))[0][0][0]

    @cherrypy.expose
    def api(self, path=None, number=None):

        # Called with `/api/version`
        if path is not None and path == 'version':
            return '''{}"lastBatchNumber": {}, "appVersion": {}{}'''\
                   .format('{', self.get_last_batch_number(), APP_VERSION, '}')

        # Called with `/api/batch?number=%d`
        elif number is not None and path == 'batch':
            # This is a template that will be filled up with data comes from database.
            json_object_template = '{}"url": {}, "blurredUrl": {}, "titleOfStory" : {}, "smallDetailOfStory": {}, ' \
                   '"fullDetailOfStory": {}, "time": {}, "videoUrl": {}{}'

            # Find id of videos in requested batch number.
            ids = [i[0] for i in self.db.run(('SELECT video_id FROM batches WHERE number={}'.format(number),))[0]]

            # Get details of videos with id stored in `video_ids`.
            details = [i[0] for i in self.db.run(['SELECT * from videos where id={}'.format(i) for i in ids])]

            # Build JSON array string with proper data.
            return '[' + ', <br>'.join([json_object_template.format('{', *i[1:], '}') for i in details]) + ']'


        # URLs that haven't been handle or requests with bad parameters.
        else:
            return self.default()

    @cherrypy.expose
    def default(self, attr=None):
        return "Page not Found!"


if __name__ == '__main__':
    cherrypy.quickstart(Server(), '/', 'server.conf')
