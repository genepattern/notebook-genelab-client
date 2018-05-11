
#singleton for ineracting with GeneLab

from genomespaceclient import GenomeSpaceClient
import genepattern
import IPython.core.display as display
from IPython.display import display_javascript

from ipywidgets import widgets
from traitlets import Unicode, Integer
import nbtools


class GSGeneLabClient:
    myGeneLabClient = None

    def testMethod(self):
        print("GSGetFile test called")

    # create the client which we need to have cache the user/pass
    def GeneLabLogin(self, username, password):
        self.myGeneLabClient = GenomeSpaceClient(username, password)
        js = """var cellIdx = IPython.notebook.get_selected_index();
            var cell =  IPython.notebook.get_cell(cellIdx+1);
            cell.set_text(cell.get_text().replace(new RegExp('foo','g'),'< PasswordHidden >'));
            // alert('Password is being hidden after use to remove it from the notebook for security reasons.');
            cell.render();""".replace('foo', password)
        jjss = display.Javascript(js)
        display.display(jjss)

        return self.myGeneLabClient

    def downloadFile(self, genelabUrl, localFileName):

        initial = display.HTML("<p>Downloading <a href='" + genelabUrl + "'>"+ genelabUrl+"</a> as " + localFileName+ "</p?")
        display.display(initial);
        self.myGeneLabClient._download_file(genelabUrl, localFileName)
        return display.HTML("<p>Done</p>")







singleton = GSGeneLabClient()


def loadGSGToolsToNBToolManager():
    print("TBD - implement loadGSGToolsToNBToolManager")
    # set up the tools
    # nbtm = nbtools.NBToolManager()
    #
    # nbtm.register(singleton.GeneLabLogin, name="GeneLab Login",
    #                             description="Login to GeneLab",
    #                             parameters={
    #                                 "username": {
    #                                     "type": "String"
    #                                 },
    #                                 "password": {
    #                                     "type": "password",
    #                                     "default": "password"
    #                                 },
    #                                 "output_var": {
    #                                     "hide": True
    #                                 }
    #                             })
    #
    # genepattern.GPUIBuilder(singleton.downloadFile, name="GeneLab Download File",
    #                       description="Download a file from GeneLab into the current directory",
    #                 parameters={
    #                 "File_URL": {
    #                     "type": "String",
    #                     "default": "https://genelab-data.ndc.nasa.gov/datamanager/file/Home/ted/GLDS-42_microarray_A-AFFY-60.adf/A-AFFY-60.adf.txt"
    #                 },
    #                 "File_Name"  :{
    #                     "type": "String",
    #                     "default": "A-AFFY-60.adf.txt"
    #                 },
    #                 "output_var": {
    #                     "hide": True
    #                 }
    # })