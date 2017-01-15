from ..utils import TranspileTestCase


class AssertTests(TranspileTestCase):
    def test_assert(self):
        self.assertCodeExecution("""
            x = 10
            print("Pre assert 1")
            assert x > 0, "It's big"
            print("Pre assert 2")
            assert x < 0, "It isn't big"
            print("Done.")
            """, exits_early=True)

    def test_assert_without_message(self):
        self.assertCodeExecution("""
            x = 10
            print("Pre assert 1")
            assert x > 0
            print("Pre assert 2")
            assert x < 0
            print("Done.")
            """, exits_early=True)
