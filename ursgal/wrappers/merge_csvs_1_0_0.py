#!/usr/bin/env python3.4
import ursgal
import os


class merge_csvs_1_0_0( ursgal.UNode ):
    """Merge CSVS 1_0_0 UNode"""
    META_INFO = {
        'edit_version'       : 1.00,                                            # flot, inclease number if something is changed (kaz)
        'name'               : 'Merge CSVs',                                    # str, Software name (kaz)
        'version'            : '1.0.0',                                         # str, Software version name (kaz)
        'release_date'       : '2016-3-4',                                      # None, '%Y-%m-%d' or '%Y-%m-%d %H:%M:%S' (kaz)
        'engine_type' : {
            'converter' : True,
        },
        'input_types'        : ['csv'],                                         # list, extensions without a dot (kaz)
        'multiple_files'     : False,                                           # bool, fill true up if multiple files input is MUST like venn-diagram (kaz)
        'output_extension'   : ['csv'],                                         # list, extensions without a dot (kaz)
        'output_suffix'      : 'merged',
        'include_in_git'     : True,
        'in_development'     : False,
        'citation'           : 'Kremer, L. P. M., Leufken, J., '\
            'Oyunchimeg, P., Schulze, S. & Fufezan, C. (2016) '\
            'Ursgal, Universal Python Module Combining Common Bottom-Up '\
            'Proteomics Tools for Large-Scale Analysis. '\
            'J. Proteome res. 15, 788-794.',
        'utranslation_style' : 'merge_csvs_style_1',
        'engine' : {
            'platform_independent' : {
                'arc_independent' : {
                    'exe' : 'merge_csvs_1_0_0.py',
                },
            },
        },
    }

    def __init__(self, *args, **kwargs):
        super(merge_csvs_1_0_0, self).__init__(*args, **kwargs)

    def _execute( self ):
        '''
        Merges .csv files

        for same header, new rows are appended

        for different header, new columns are appended
        '''
        print('[ -ENGINE- ] Merging csv files...')
        self.time_point(tag = 'execution')
        csv_files = []

        for input_file_dict in self.params['input_file_dicts']:
            csv_files.append(
                os.path.join(
                    input_file_dict['dir'],
                    input_file_dict['file']
                )
            )

        self.params['translations']['output_file_incl_path'] = os.path.join(
            self.params['output_dir_path'],
            self.params['output_file']
        )

        merge_csv_main = self.import_engine_as_python_function()
        merged_csv_output_path = merge_csv_main(
            csv_files = csv_files,
            output    = self.params['translations']['output_file_incl_path'],
        )
        self.print_execution_time(tag='execution')
        return merged_csv_output_path
