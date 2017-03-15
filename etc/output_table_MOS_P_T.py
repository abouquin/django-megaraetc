def tablenewpsfMPT(lambdaeff_string, seeingx_string,
seeing_centermean_string, seeing_cr1_string,
sncont_centerspaxel_voxel_string, sncont_cr1spaxels_voxel_string,
tsncont_centerspaxel_voxel_string, tsncont_cr1spaxels_voxel_string,
sncont_centerspaxel_aa_string, sncont_cr1spaxels_aa_string,
tsncont_centerspaxel_aa_string, tsncont_cr1spaxels_aa_string,
sncont_centerspaxel_all_string, sncont_cr1spaxels_all_string,
tsncont_centerspaxel_all_string, tsncont_cr1spaxels_all_string):
    tablenewpsfstring = '<hr />' + \
                        'OUTPUT CONTINUUM SNR' + \
                        '<br />(at lambda_c(VPH) = ' + lambdaeff_string + ' AA)' + \
                        '<table border=1>' + \
                        '<tr><th class="iconcolumn" scope="col"> </th>' + \
                            '<th scope="col" colspan="5">* Continuum SNR per spaxel zones due to PSF (MOS mode):<br />' + \
                            'fiber diameter=0.62 arcsec; Seeing FWHM=' + seeingx_string + ' arcsec</th>' + \
                            '</tr>' + \
                        '<tr><th class="iconcolumn" scope="row"></th>' + \
                            '<th scope="col" colspan="2" class="perframecolumn">** per frame</th>' + \
                            '<th scope="col" colspan="2" class="allframecolumn">** all frames</th>' + \
                            '<td></td>' + \
                            '</tr>' + \
                        '<tr><th class="iconcolumn" scope="row"><img class="iconsize" src="/static/etc/images/icon_psfrings.jpeg" /></th>' + \
                            '<td class="colc"><img class="iconsize" src="/static/etc/images/icon_psfrings_c.jpeg"><br />C<br />(' + seeing_centermean_string +'%)<br />1 fiber</td>' + \
                            '<td class="colcr1"><img class="iconsize" src="/static/etc/images/icon_psfrings_cr1.jpeg"><br />C+R1<br />(' + seeing_cr1_string + '%)<br />7 fibers</td>' + \
                            '<td class="colc"><img class="iconsize" src="/static/etc/images/icon_psfrings_c.jpeg"><br />C<br />(' + seeing_centermean_string + '%)<br />1 fiber</td>' + \
                            '<td class="colcr1"><img class="iconsize" src="/static/etc/images/icon_psfrings_cr1.jpeg"><br />C+R1<br />(' + seeing_cr1_string + '%)<br />7 fibers</td>' + \
                            '<td></td>' + \
                            '</tr>' + \
                        '<tr><td class="iconcolumn"><img class="iconsize" src="/static/etc/images/icon_pspfwhm.jpeg" /></td>' + \
                            '<td class="perframecolumn"> ' + sncont_centerspaxel_voxel_string + ' </td>' + \
                            '<td> ' + sncont_cr1spaxels_voxel_string + '</td>' + \
                            '<td class="perframecolumn"> ' + tsncont_centerspaxel_voxel_string + ' </td>' + \
                            '<td> ' + tsncont_cr1spaxels_voxel_string + '</td>' + \
                            '<td> per voxel</td>' + \
                            '</tr>' + \
                        '<tr><td class="iconcolumn"><img class="iconsize" src="/static/etc/images/icon_peraa.jpeg" /></td>' + \
                            '<td class="perframecolumn"> ' + sncont_centerspaxel_aa_string + ' </td>' + \
                            '<td> ' + sncont_cr1spaxels_aa_string + '</td>' + \
                            '<td class="perframecolumn"> ' + tsncont_centerspaxel_aa_string + ' </td>' + \
                            '<td> ' + tsncont_cr1spaxels_aa_string + '</td>' + \
                            '<td> per AA</td>' + \
                            '</tr>' + \
                        '<tr><td class="iconcolumn"><img class="iconsize" src="/static/etc/images/icon_integrated.jpeg" /></td>' + \
                            '<td class="perframecolumn"> ' + sncont_centerspaxel_all_string + ' </td>' + \
                            '<td> ' + sncont_cr1spaxels_all_string + '</td>' + \
                            '<td class="perframecolumn"> ' + tsncont_centerspaxel_all_string + ' </td>' + \
                            '<td> ' + tsncont_cr1spaxels_all_string + '</td>' + \
                            '<td> integrated spectrum </td>' + \
                            '</tr>' + \
                        '</table><br />'
                        # 'TESTING AREA: SNCONT_C_VOXEL= ' + sncont_centerspaxel_voxel_string + '<br />' + \
                        # 'TESTING AREA: SNCONT_R1_VOXEL= ' + sncont_r1spaxel_voxel_string + '<br />'
    return tablenewpsfstring