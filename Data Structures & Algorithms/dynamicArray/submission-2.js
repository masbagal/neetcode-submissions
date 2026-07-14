class DynamicArray {
    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {
        this.array = new Array(this.capacity)
        this.size = 0
        this.capacity = capacity
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        return this.array[i]
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.array[i] = n
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {
        if (this.size === this.capacity) {
            this.resize()
        }
        this.array[this.size] = n
        this.size += 1
    }

    /**
     * @returns {number}
     */
    popback() {
        const value = this.array[this.size - 1]
        this.array[this.size - 1] = null
        this.size -= 1
        return value
    }

    /**
     * @returns {void}
     */
    resize() {
        this.capacity *= 2
        const newArray = new Array(this.capacity)
        for (let i = 0; i < this.size; i++) {
            newArray[i] = this.array[i]
        }
        this.array = newArray
    }

    /**
     * @returns {number}
     */
    getSize() {
        return this.size
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity
    }
}
