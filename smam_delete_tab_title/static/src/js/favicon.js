/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { patch } from "web.utils";

patch(WebClient.prototype, "odoo-custom-module-aldim.WebClient", {
    setup() {
        this._super();
        this.title.setParts({ zopenerp: "SMAM" });
    },
});