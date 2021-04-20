import XCTest
@testable import swift_exp

final class swift_expTests: XCTestCase {
    func testExample() {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct
        // results.
        XCTAssertEqual(swift_exp().text, "Hello, World!")
    }

    static var allTests = [
        ("testExample", testExample),
    ]
}
