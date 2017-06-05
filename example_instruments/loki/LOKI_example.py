from nexusbuilder import NexusBuilder

if __name__ == '__main__':
    builder = NexusBuilder('LOKI_example_gzip.hdf5', idf_filename='LOKI_Definition.xml',
                           compress_type='gzip', compress_opts=1)
    builder.add_user('LOKI Team', 'ESS')
    builder.add_dataset('/raw_data_1/', 'definition', 'TOFRAW',
                        {'url': 'http://definition.nexusformat.org/instruments/TOFRAW?version=1.0'})
