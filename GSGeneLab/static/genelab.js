requirejs(["nbtools", "jquery"], function(NBToolManager, $) {
    // no return unless something else is dependent on this?

    const GSGLLoginWidgetTool = new NBToolManager.NBTool({
        origin: "+",
        id: "gsgl_Login",
        name: "GeneLab_Login",
        description: "Login to GeneLab to allow files to be up/downloaded.",
        load: function() {

             return true; },
        render: function() {
            let cell = Jupyter.notebook.get_selected_cell();
            const is_empty = cell.get_text().trim() === "";
            if (!is_empty) {
                cell = Jupyter.notebook.insert_cell_below();
                Jupyter.notebook.select_next();
            }
            cell.set_text("import GSGeneLab\nimport genepattern\n"
                   + "genepattern.GPUIBuilder(GSGeneLab.singleton.GeneLabLogin,\n\tparameters={"
                   + "'username': { 'type': 'String' }, 'password': { 'type': 'Password' }, 'output_var': { 'hide': 'True' } }"
                   + ", function_import='gs.singleton.GeneLabLogin')")
            // execute cell
            cell.execute()

            return cell;
        }
    });
    NBToolManager.instance().register(GSGLLoginWidgetTool)


    const GSGLDownloadWidgetTool = new NBToolManager.NBTool({
        origin: "+",
        id: "gsgl_GetDownload",
        name: "GetGeneLabFile",
        description: "Select a GeneLab file and have it downloaded to the notebook server. Make sure to do a GeneLab login first.",
        load: function() {

             return true; },
        render: function() {
            let cell = Jupyter.notebook.get_selected_cell();
            const is_empty = cell.get_text().trim() === "";
            if (!is_empty) {
                cell = Jupyter.notebook.insert_cell_below();
                Jupyter.notebook.select_next();
            }
            getFileUrlFromGeneLab(cell);
            // If this cell is not empty, insert a new cell and use that
            // Otherwise just use this cell

            return cell;
        }
    });
    NBToolManager.instance().register(GSGLDownloadWidgetTool)





    function getFileUrlFromGeneLab(cell){
        var jsuiRoot = "https://genelab-data.ndc.nasa.gov/jsui";
        var gsUploadUrl = jsuiRoot +"/jsCDK/loadUrlToGenomespace.html?";

        var returnListener = function(e){

            window.removeEventListener("message", returnListener, false);
            //cell.set_text("gs.singleton.downloadFile(\'"+ e.data.destination+"\', 'fileFromGenelab')")
            var glurl = e.data.destination;

            var defaultName = glurl.substring(glurl.lastIndexOf("/") + 1);

            cell.set_text("import GSGeneLab\nimport genepattern\n"
                   + "genepattern.GPUIBuilder(GSGeneLab.singleton.downloadFile,\n\tparameters={"
                   + "'genelabUrl': { 'type': 'String', 'default': '"+ e.data.destination+"' }, 'localFileName': { 'type': 'String', 'default':'"+defaultName+"' }, 'output_var': { 'hide': 'True' } }"
                   + ", function_import='gs.singleton.downloadFile')")


            // execute cell
            cell.execute()
        };

        var newWin = window.open(gsUploadUrl  + "getLocation=True&action=IMPORT&selectType=FILE", "GeneLab Import", "height=340px,width=550px");
        newWin.focus();

        window.addEventListener( "message",  returnListener);

    }


});
