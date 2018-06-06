# ElasticQuery
# File: tests/util.py
# Desc: quick assert_equal wrapper to use dictdiffer and print the expected/output

from dictdiffer import diff as dictdiff


def assert_equal(self, output, expected):
    try:
        self.assertEqual(output, expected)
    except AssertionError as e:
        print('OUTPUT', output)
        print('EXPECTED', expected)

        diff = list(dictdiff(output, expected))
        for d in diff:
            print(d)

        raise e
