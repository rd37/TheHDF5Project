namespace cpp raven.commons
namespace java raven.commons
namespace js raven.commons
namespace py raven.commons.audio_enc

enum Layout {
    INTERLEAVED,
    NON_INTERLEAVED
}

struct Audio {
    1: required i64 timestamp;
    2: required i32 rate;
    3: required i32 channels;
    4: required Layout layout = Layout.INTERLEAVED;
    6: required list<double> sample;
}
